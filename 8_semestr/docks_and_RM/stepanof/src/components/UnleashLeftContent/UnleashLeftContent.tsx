import s from './UnleashLeftContent.module.scss'
import sE from './ExploreMoreBtn.module.scss'

export const UnleashLeftContent = () => {
  const text = [
    'Best Seller All Around World',
    '$2M+ Transections Every Day',
    'Secure Transactions',
    'Exclusive Collections From Sellers',
    'Easy Buying and Selling',
    'Join Our Community',
  ]

  return (
    <div className={s.unleash__left_content}>
      <span>Just Unleash -</span>
      <span>Your Inner Collector</span>
      <ul className={s.unleash__list}>
        {text.map((item, index) => (
          <li
            className={s.unleash__list_item}
            key={index}
          >
            <img
              src="img/chek.svg"
              alt="check"
            />
            <span>{item}</span>
          </li>
        ))}
      </ul>
      <button className={sE.explore_more_btn}>
        <span>Explore More</span>
        <img
          src="img/arrow-explore.svg"
          alt="arrow"
        />
      </button>
    </div>
  )
}
