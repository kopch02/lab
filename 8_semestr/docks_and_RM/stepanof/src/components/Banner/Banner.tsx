import s from './Banner.module.scss'

export const Banner = () => {
  return (
    <div className={s.banner}>
      <div className={s.banner__left_content}>
        <h2>Create and Sell NFTs</h2>
        <p>World’s Largest NFT Place</p>
        <div className={s.banner__action}>
          <button className={s.more}>Explore More</button>
          <button className={s.sell}>Sell Artwork</button>
        </div>
      </div>
      <div className={s.banner__img}>
        <img
          src="img/banner1.jpg"
          alt="banner1"
          className={s.banner__banner1}
        />
        <img
          src="img/banner2.jpg"
          alt="banner2-blure"
          className={s.banner__banner2_blure}
        />
      </div>
    </div>
  )
}
