import React from 'react'

import s from './Order.module.scss'

export const Order = () => {
  return (
    <div className={s.content}>
      <div className={s.order}>
        <span className={s.comission}>Задолжность: 4300р</span>
        <button className={s.pay}>Оплатить</button>
      </div>
    </div>
  )
}
