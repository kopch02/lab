export interface ITrendingItem {
  id: number
  image: string
  name: string
  bid: string
  time: string
}

export interface ISellers {
  id: number
  image: string
  name: string
  username: string
}

export interface IRecentlyItem {
  id: number
  image: string
  name: string
  username: string
  price: string
  procent: number
}

export interface ICollections {
  id: number
  image: string
  name: string
  username: string
  volume: string
  procent: number
  price: string
  owners: string
  items: string
}
