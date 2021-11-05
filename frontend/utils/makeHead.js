// todo:後でurl毎修正する
export default function (title, description, image) {
  let imageAbsoluteUrl = image
  if (typeof image === 'string' && imageAbsoluteUrl.slice(0, 1) === '/') {
    imageAbsoluteUrl = 'https://nodaridaisai.com' + imageAbsoluteUrl
  }
  const defaultImageUrl = 'https://nodaridaisai.com' + require('~/assets/images/logo.png')
  const imageUrl = imageAbsoluteUrl || defaultImageUrl

  return {
    title: title ? `${title} - nikki de kakeibo` : '野田地区理大祭2021',
    meta: [
      { hid: 'description', name: 'description', content: description || '2021年度東京理科大学野田地区理大祭公式ウェブサイト。本年度は9月20日(月・祝)、21日(火)の2日間開催。' },
      // Twitter Card
      { hid: 'twitter:card', name: 'twitter:card', content: 'summary_large_image' },
      { hid: 'twitter:site', name: 'twitter:site', content: '@noda_ridaisai' },
      { hid: 'twitter:title', name: 'twitter:title', content: title || '2021年度野田地区理大祭' },
      { hid: 'twitter:description', name: 'twitter:description', content: description || '2021年度東京理科大学野田地区理大祭公式ウェブサイト。本年度は9月20日(月・祝)、21日(火)の2日間開催。' },
      { hid: 'twitter:image', name: 'twitter:image', content: imageUrl } // ← ここのURLを変えるのも忘れずに！
    ]
  }
}
