import { createElectronRouter } from 'electron-router-dom'
import { ROUTER_IDS } from '@globaltype/router'

export const { Router, registerRoute } = createElectronRouter({
  port: 5173,
  types: {
    ids: [...ROUTER_IDS]
  }
})
