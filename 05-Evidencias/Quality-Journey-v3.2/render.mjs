import fs from 'node:fs/promises';
import path from 'node:path';
import { FileBlob, PresentationFile } from '@oai/artifact-tool';
const [source, out] = process.argv.slice(2);
if (!source || !out) throw new Error('Uso: node render.mjs fonte.pptx pasta-saida');
const presentation = await PresentationFile.importPptx(await FileBlob.load(source));
await fs.mkdir(out, { recursive: true });
for (const [i, slide] of presentation.slides.items.entries()) {
  const png = await presentation.export({ slide, format: 'png', scale: 1 });
  await fs.writeFile(path.join(out, `slide-${String(i+1).padStart(2,'0')}.png`), new Uint8Array(await png.arrayBuffer()));
}
// Importação e exportação de imagens somente; não exportar/sobrescrever PPTX.
console.log(JSON.stringify({ slides: presentation.slides.items.length, sourceUnmodified: true }));
