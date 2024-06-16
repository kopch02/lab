import s from './Hero.module.scss'

export const Hero = () => {
  return (
    <div className={s.main_section}>
      <div className={s.hero_text}>
        <div className={s.line}></div>
        <div className={s.hero_content}>
          <h1>Discover And Create NFTs</h1>
          <p>
            Discover, Create and Sell NFTs On Our NFT Marketplace With Over
            Thousands Of NFTs And Get a <strong>$20 bonus.</strong>
          </p>
        </div>
        <div className={s.hero_btns}>
          <a href="#explore-more">
            <button className={s.more}>Explore More</button>
          </a>
          <button className={s.create}>create NFT</button>
        </div>
        <div className={s.features}>
          <ul className={s.features__list}>
            <li className={s.features__list_item}>
              <span className={s.features__list_main}>430K+</span>
              <span className={s.features__list_side}>Art Works</span>
            </li>
            <li className={s.features__list_item}>
              <span className={s.features__list_main}>159K+</span>
              <span className={s.features__list_side}>Creators</span>
            </li>
            <li className={s.features__list_item}>
              <span className={s.features__list_main}>87K+</span>
              <span className={s.features__list_side}>Collections</span>
            </li>
          </ul>
        </div>
      </div>

      <div className={s.hero_header}>
        <img
          src="img/header1.jpg"
          alt="header1"
          className={s.hero_header__header1}
        />
        <img
          src="img/header1.jpg"
          alt="header1-blure"
          className={s.hero_header__header1_blure}
        />
        <img
          src="img/arrow.svg"
          alt="arrow"
          className={s.hero_header__arrow}
        />
        <img
          src="img/header2.jpg"
          alt="header2"
          className={s.hero_header__header2}
        />
        <img
          src="img/header2.jpg"
          alt="header2-blure"
          className={s.hero_header__header2_blure}
        />
        <img
          src="img/dots.svg"
          alt="dots"
          className={s.hero_header__dots}
        />
      </div>
    </div>
  )
}
