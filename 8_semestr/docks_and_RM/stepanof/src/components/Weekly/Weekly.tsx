import { useEffect, useState } from 'react'

import { getItem } from '../../api/api'
import { ITrendingItem } from '../../types/types'
import { TrendingItem } from '../TrendingItem/TrendingItem'
import { RecentlyView } from '../RecentlyView/RecentlyView'
import s from './Weekly.module.scss'

export const Weekly = () => {
  const [trendingData, setTrendingData] = useState<ITrendingItem[]>([])

  const fetchItems = async () => {
    try {
      setTrendingData(await getItem())
    } catch (error) {
      throw new Error('Ошибка')
    }
  }

  useEffect(() => {
    fetchItems()
  }, [])

  return (
    <div className={s.weekly}>
      <h2>Weekly - Top NFT</h2>
      <div className={s.weekly_container}>
        <ul className={s.trending}>
          {trendingData.slice(0, 5).map((item) => (
            <TrendingItem
              key={item.id}
              item={item}
            />
          ))}
        </ul>
        <div className={s.recently}>
          <RecentlyView data={120} />
        </div>
      </div>
    </div>
  )
}
