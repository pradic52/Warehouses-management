import { ipcRenderer } from 'electron'

// Custom APIs for renderer
const api = {
  invoke: (channel: string, data?: unknown) => ipcRenderer.invoke(channel, data),
  isFirstRun: () => ipcRenderer.invoke('is-first-run'),
  completeSetup: (data: unknown) => ipcRenderer.send('setup-complete', data)
}

export default api
