import { useState } from 'react'

import s from './Header.module.scss'

export const Header = () => {
  const [openMenu, setOpenMenu] = useState(false)

  return (
    <header className={s.header}>
      <div className={s.logo}>
        <a href="/">
          <img
            src="img/logo.jpg"
            alt="logo"
          />
        </a>
        <span>DiveSea</span>
      </div>
      <nav className={s.nav}>
        <button
          className={s.nav_mobile_btn}
          id="nav_btn"
          onClick={() => setOpenMenu(!openMenu)}
        >
          <img
            src="img/menu.svg"
            alt="menu"
          />
        </button>
        <ul
          className={`${s.nav__list} ${openMenu ? s.nav__list_active : ''}`}
          id="nav__list"
        >
          <li className={s.nav__list_item}>
            <a
              href="/"
              className={s.nav__list_link}
            >
              Главная
            </a>
          </li>
          <li className={s.nav__list_item}>
            <a
              href="/forms"
              className={s.nav__list_link}
            >
              Заказать
            </a>
          </li>
          <li className={s.nav__list_item}>
            <a
              href="/system"
              className={s.nav__list_link}
            >
              Книги
            </a>
          </li>
          <li className={s.nav__list_item}>
            <a
              href="/order"
              className={s.nav__list_link}
            >
              Оплата
            </a>
          </li>
        </ul>
      </nav>
    </header>
  )
}
