import s from './Footer.module.scss'

export const Footer = () => {
  return (
    <div className={s.footer}>
      <div className={s.container}>
        <div className={s.unit}>
          <div className={s.footer__logo}>
            <img
              src="img/footer-logo.svg"
              alt="logo"
            />
            <span>DiveSea</span>
          </div>
          <ul className={s.footer__menu}>
            <li>Privacy Policy</li>
            <li>Term &#38; Conditions</li>
            <li>About Us</li>
            <li>Contact</li>
          </ul>
        </div>
        <div className={s.footer__line}></div>
        <div className={s.footer__lower}>
          <span>© 2023 EATLY All Rights Reserved</span>
          <ul className={s.footer__social}>
            <img
              src="img/inst-logo.svg"
              alt="inst-logo"
            />
            <img
              src="img/in-logo.svg"
              alt="in-logo"
            />
            <img
              src="img/facebook-logo.svg"
              alt="facebook-logo"
            />
            <img
              src="img/tweeter-logo.svg"
              alt="tweeter-logo"
            />
          </ul>
        </div>
      </div>
    </div>
  )
}
