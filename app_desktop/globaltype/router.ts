export const ROUTER_IDS = ['main', 'setup'] as const

export type RouterId = (typeof ROUTER_IDS)[number]

export type RouterIds = typeof ROUTER_IDS
