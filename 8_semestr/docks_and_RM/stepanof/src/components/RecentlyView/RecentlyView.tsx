import { useEffect, useState } from 'react'

import { IRecentlyItem } from '../../types/types'
import { getRecently } from '../../api/api'
import s from './RecentlyView.module.scss'

interface IProps {
  data: number
}

export const RecentlyView = ({ data }: IProps) => {
  const [recentData, setTrendingData] = useState<IRecentlyItem[]>([])

  const fetchItems = async () => {
    try {
      setTrendingData(await getRecently())
    } catch (error) {
      throw new Error('Ошибка')
    }
  }

  useEffect(() => {
    fetchItems()
  }, [])

  return (
    <div
      className={s.recently__view}
      style={{ transform: `translateX(${data}%)` }}
    >
      <div className={s.recently__top}>
        <h3>Recent Viewed</h3>
        <img
          src="img/dots-mini.svg"
          alt="dots"
        />
      </div>
      <ul className={s.recently__list}>
        {recentData.map((item, index) => (
          <li
            className={s.recently__list_item}
            key={index}
          >
            <div className={s.recently__icon}>
              <img
                src={item.image}
                alt={`recently${index + 1}`}
                className={s.recently__item_img}
              />
              <div className={s.recently__item_number}>
                <span>{index + 1}</span>
              </div>
              <div className={s.recently__item_name}>
                <span className={s.recently__name_span1}>{item.name}</span>
                <span className={s.recently__name_span2}>{item.username}</span>
              </div>
            </div>
            <div className={s.recently__item_price_container}>
              <div className={s.recently__item_price}>
                <img
                  src="img/evirium.svg"
                  alt="evirium-logo"
                  className={s.efirium_logo}
                />
                <span>{item.price}</span>
              </div>
              <span
                className={s.recently__item_procent}
                style={{ color: item.procent > 0 ? 'green' : 'red' }}
              >
                {item.procent > 0 ? `+${item.procent}%` : `${item.procent}%`}
              </span>
            </div>
          </li>
        ))}
      </ul>
    </div>
  )
}
