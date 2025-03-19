import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'



// https://vite.dev/config/
export default defineConfig({
    presets: [
        '@vue/cli-plugin-babel/preset'
    ],
    plugins: [
        vue()
    ],


})
