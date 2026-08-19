import fs from "node:fs/promises";
import path from "node:path";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const [workbookPath, previewDir] = process.argv.slice(2);
const workbook = await SpreadsheetFile.importXlsx(await FileBlob.load(workbookPath));
await fs.mkdir(previewDir, { recursive: true });
console.log((await workbook.inspect({kind: "sheet", include: "id,name", maxChars: 5000})).ndjson);
console.log((await workbook.inspect({kind: "table", sheetId: "LEIA-ME", range: "A1:B10", tableMaxRows: 12, tableMaxCols: 4, maxChars: 5000})).ndjson);
console.log((await workbook.inspect({kind: "match", searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A", options: {useRegex: true, maxResults: 100}, summary: "formula errors", maxChars: 5000})).ndjson);
for (const sheet of workbook.worksheets) {
  const image = await workbook.render({sheetName: sheet.name, autoCrop: "all", scale: 1, format: "png"});
  await fs.writeFile(path.join(previewDir, `${sheet.index + 1}-${sheet.name}.png`), new Uint8Array(await image.arrayBuffer()));
}
