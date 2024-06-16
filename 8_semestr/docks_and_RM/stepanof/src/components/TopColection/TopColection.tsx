import { useEffect, useState } from 'react'

import { CollectionItem } from '../СollectionItem/CollectionItem'
import { ICollections } from '../../types/types'
import { getCollection } from '../../api/api'
import { ExploreAllArrow } from '../ExploreAllArrow/ExploreAllArrow'
import s from './TopColection.module.scss'

export const TopColection = () => {
  const [collectionData, setCollectionData] = useState<ICollections[]>([])

  const fetchItem = async () => {
    try {
      setCollectionData(await getCollection())
    } catch (error) {
      throw new Error('ошибка')
    }
  }

  useEffect(() => {
    fetchItem()
  }, [])

  return (
    <div className={s.top_collection}>
      <h2 className={s.top_collection__header}>Top Collection</h2>
      <table className={s.collection_table}>
        <thead>
          <tr className={s.filter}>
            <th style={{ textAlign: 'left' }}>Collection</th>
            <th>Volume</th>
            <th>24h %</th>
            <th>Floor Price</th>
            <th>Owners</th>
            <th>Items</th>
          </tr>
        </thead>
        <tbody>
          {collectionData.map((item) => (
            <CollectionItem
              item={item}
              key={item.id}
            />
          ))}
        </tbody>
      </table>
      <ExploreAllArrow />
    </div>
  )
}
