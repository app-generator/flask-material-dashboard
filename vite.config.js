import { defineConfig } from "vite";
import autoprefixer from "autoprefixer";
import cssnano from "cssnano";
import path from "path";
import fs from "fs";

export default defineConfig(({ mode }) => {
    const isProduction = mode === "production";

    const scssDirectory = path.resolve(__dirname, "static/assets/scss");
    const scssFiles = fs.readdirSync(scssDirectory)
        .filter(file => file.endsWith(".scss"))
        .map(file => path.resolve(scssDirectory, file));

    return {
        css: {
            postcss: {
                plugins: [
                    autoprefixer(),
                    isProduction && cssnano(),
                ].filter(Boolean),
            },
        },
        build: {
            outDir: "static",
            emptyOutDir: false,
            rollupOptions: {
                input: scssFiles,
                output: {
                    assetFileNames: "assets/css/[name].css",
                },
            },
        },
    };
});
