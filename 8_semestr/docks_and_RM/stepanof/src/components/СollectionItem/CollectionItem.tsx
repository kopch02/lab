import { ICollections } from '../../types/types'
import s from './СollectionItem.module.scss'

interface IProps {
  item: ICollections
}

export const CollectionItem = ({ item }: IProps) => {
  return (
    <tr className={s.collection_table_row}>
      <td className={s.collection_logo}>
        <img
          src={item.image}
          alt="recently1"
          className={s.collection_logo_img}
        />
        <div className={s.collection_item_name}>
          <span className={s.collection_name_span1}>{item.name}</span>
          <span className={s.collection_name_span2}>{item.username}</span>
        </div>
      </td>
      <td>
        <img
          src="img/evirium.svg"
          alt="evirium-logo"
          className={s.collection_efirium_logo}
        />
        <span className={s.collection_efirium_logo_span}>{item.volume}</span>
      </td>
      <td
        className={s.collection_item_list_item_procent}
        style={{ color: item.procent > 0 ? 'green' : 'red' }}
      >
        {item.procent > 0 ? `+${item.procent}%` : `${item.procent}%`}
      </td>
      <td>
        <img
          src="img/evirium.svg"
          alt="evirium-logo"
          className={s.collection_efirium_logo}
        />
        <span className={s.collection_efirium_logo_span}>{item.price}</span>
      </td>
      <td className={s.collection_item_list_item}>{item.owners}</td>
      <td className={s.collection_item_list_item}>{item.items}</td>
    </tr>
  )
}
