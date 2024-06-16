import s from './Notification.module.scss'

export const Notification = () => {
  return (
    <div className={s.unleash_notification}>
      <div className={s.unleash_notification__info}>
        <div className={s.unleash_notification__info_logo}>
          <img
            src="./img/point.svg"
            alt="point"
            className={s.unleash_notification__info_logo_img}
          />
          <div className={s.unleash_notification__avatar}>
            <img
              src="./img/notofication-avatar.jpg"
              alt="avatar"
              className={s.unleash_notification__avatar_img}
            />
            <img
              src="./img/verified.svg"
              alt="verified"
              className={s.unleash_notification__avatar_verified}
            />
          </div>
        </div>
        <div className={s.unleash_notification__info_text}>
          <div className={s.unleash_notification__info_name}>
            <span>New bid</span>
            <span>Rotation</span>
          </div>
          <span>0.002 ETH</span>
          <span>6 Oct 2022, 11:44 PM</span>
        </div>
      </div>
      <img
        src="./img/notofication-logo.jpg"
        alt="notofication-logo"
        className={s.unleash_notification__logo}
      />
    </div>
  )
}
