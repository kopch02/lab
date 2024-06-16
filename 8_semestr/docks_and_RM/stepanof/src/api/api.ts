import axios from 'axios'

const baseApi = import.meta.env.VITE_BASE_API || 'http://localhost:3004'

const instance = axios.create({
  baseURL: baseApi,
})

export const getItem = async () => {
  const { data } = await instance.get('/cards')
  return data
}

export const getSellers = async () => {
  const { data } = await instance.get('/sellers')
  return data
}

export const getRecently = async () => {
  const { data } = await instance.get('/recently')
  return data
}

export const getCollection = async () => {
  const { data } = await instance.get('/collections')
  return data
}

export const getPassword = async () => {
  const { data } = await instance.get('/password')
  return data
}
