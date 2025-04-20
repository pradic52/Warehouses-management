import { defineConfig, externalizeDepsPlugin } from 'electron-vite'
import react from '@vitejs/plugin-react'
import tsconfigPaths from 'vite-tsconfig-paths'
import path from 'path'

export default defineConfig({
  main: {
    plugins: [externalizeDepsPlugin()],
    resolve: {
      alias: {
        '@globaltype': path.resolve(__dirname, 'globaltype')
      }
    }
  },
  preload: {
    plugins: [externalizeDepsPlugin()],
    resolve: {
      alias: {
        '@globaltype': path.resolve(__dirname, 'globaltype')
      }
    }
  },
  renderer: {
    plugins: [react(), tsconfigPaths()]
  }
})
