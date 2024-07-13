import {fileURLToPath, URL} from 'node:url'

import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [
        vue(),
    ],
    build: {
        outDir: '../static', // 设置打包输出目录
        emptyOutDir: true, // 自动清空输出目录
    },
    base: './', // 设置公共路径为相对路径
    resolve: {
        alias: {
            '@': fileURLToPath(new URL('./src', import.meta.url))
        }
    }, server: {
        host: '0.0.0.0',
    }
})
