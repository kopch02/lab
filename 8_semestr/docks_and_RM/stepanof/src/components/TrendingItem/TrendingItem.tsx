import { ITrendingItem } from '../../types/types'
import s from './TrendingItem.module.scss'

interface IProps {
  item: ITrendingItem
}

export const TrendingItem = ({ item }: IProps) => {
  return (
    <li className={s.trending__item}>
      <div className={s.trending__item__image__container}>
        <img
          className={s.trending__item__main__img}
          src={item.image}
          alt="trending1"
        />
        <div className={s.trending__item__time}>
          <span>{item.time}</span>
        </div>
      </div>
      <span className={s.trending__item__main}>{item.name}</span>
      <div className={s.trending__item__side}>
        <div className={s.trending__item__side__text}>
          <span>Current bid</span>
          <div className={s.trending__item__price}>
            <img
              src="img/evirium.svg"
              alt="evirium-logo"
            />
            <span>{item.bid}</span>
          </div>
        </div>
        <button className={s.bit__btn}>PLACE BID</button>
      </div>
    </li>
  )
}
