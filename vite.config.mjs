import { defineConfig } from "vite";
import { resolve } from "path";

export default defineConfig({
    base: "/static/",
    publicDir: resolve("./frontend/public"),
    build: {
      manifest: "manifest.json",
      outDir: resolve("./bakerydemo/static"),
      emptyOutDir: true,
      rollupOptions: {
        input: {
          app: resolve("./frontend/src/application/app.js")
        }
      }
    }
  })