import s from './UnleashRightContent.module.scss'
import { Notification } from '../notification/Notification'
import { RecentlyView } from '../RecentlyView/RecentlyView'
import { BestSellers } from '../BestSellers/BestSellers'

export const UnleashRightContent = () => {
  return (
    <div className={s.unleash__right_content}>
      <RecentlyView data={0} />
      <BestSellers />
      <Notification />
    </div>
  )
}
