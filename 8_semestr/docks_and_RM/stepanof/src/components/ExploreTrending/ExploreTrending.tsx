import { useEffect, useState } from 'react'

import { getItem } from '../../api/api'
import { ITrendingItem } from '../../types/types'
import { TrendingItem } from '../TrendingItem/TrendingItem'
import s from './ExploreTrending.module.scss'

export const ExploreTrending = () => {
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
    <div className={s.explore}>
      <h2
        className={s.explore__header}
        id="explore-more"
      >
        Explore Marketplace
      </h2>
      <ul className={s.explore_filters_list}>
        <button className={s.explore_filter_item}>
          <span>All</span>
        </button>
        <button className={s.explore_filter_item}>
          <img
            src="img/categori-filter-logo.svg"
            alt="categori-filter-logo"
          />
          <span>Category</span>
        </button>
        <button className={s.explore_filter_item}>
          <img
            src="img/collection-filter-logo.svg"
            alt="collection-filter-logo"
          />
          <span>Collection</span>
        </button>
        <button className={s.explore_filter_item}>
          <img
            src="img/price-filter-logo.svg"
            alt="price-filter-logo"
          />
          <span>Price</span>
        </button>
      </ul>
      <div className={s.explore_trending}>
        <ul className={s.trending__list}>
          {trendingData.map((item) => (
            <TrendingItem
              key={item.id}
              item={item}
            />
          ))}
        </ul>
      </div>
    </div>
  )
}
