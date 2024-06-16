import { useEffect, useState } from 'react'

import { getSellers } from '../../api/api'
import { ISellers } from '../../types/types'
import s from './BestSellers.module.scss'

export const BestSellers = () => {
  const [sellersData, setTrendingData] = useState<ISellers[]>([])

  const fetchItems = async () => {
    try {
      setTrendingData(await getSellers())
    } catch (error) {
      throw new Error('Ошибка')
    }
  }

  useEffect(() => {
    fetchItems()
  }, [])

  return (
    <div className={s.best_sellers}>
      <div className={s.best_sellers__top}>
        <span className={s.best_sellers__name}>Best Sellers</span>
        <img
          src="img/dots-mini.svg"
          alt="dots"
        />
      </div>
      <div className={s.best_sellers__list}>
        {sellersData.map((item, index) => (
          <li
            className={s.best_sellers__list_item}
            key={item.id}
          >
            <div className={s.recently__icon}>
              <img
                src={item.image}
                alt={'recently${index + 1}'}
                className={s.recently__item_img}
              />
              <div className={s.best_sellers__list_item_number}>
                <span>{index + 1}</span>
              </div>
              <div className={s.recently__item_name}>
                <span className={s.recently__name_span1}>{item.name}</span>
                <span className={s.recently__name_span2}>{item.username}</span>
              </div>
            </div>
            <button className={s.best_sellers__list_item_btn}>Follow</button>
          </li>
        ))}
      </div>
    </div>
  )
}
