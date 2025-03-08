export interface Politician {
  name: string
  url: string
  fact: string
}

const politicians = [
  {
    name: 'Donald Trump',
    url: 'https://npr.brightspotcdn.com/dims3/default/strip/false/crop/4890x3260+0+0/resize/1100/quality/50/format/jpeg/?url=http%3A%2F%2Fnpr-brightspot.s3.amazonaws.com%2Feb%2F26%2F3424469c4d29b63b0b2683c3a4f2%2Fap24161743821924.jpg',
    fact: "45th U.S. President, known for his 'America First' policies.",
  },
  {
    name: 'Justin Trudeau',
    url: 'https://assets.weforum.org/sf_account/image/UgD8pKdNbiwi8GQQZxl49hBZxQs1xp1V1incce1bSBc.jpg',
    fact: "Canada's Prime Minister, leading the Liberal Party since 2015.",
  },
  {
    name: 'Claudia Sheinbaum',
    url: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTm9qxnzZJSRSKFBiZLdQ17ym5jndDCNVbxDQ&s',
    fact: 'Mayor of Mexico City, a scientist and environmental engineer.',
  },
  {
    name: 'Xi Jinping',
    url: 'https://upload.wikimedia.org/wikipedia/commons/0/04/Xi_Jinping_%28November_2024%29_02.jpg',
    fact: "China's most powerful leader promoting 'socialism with characteristics'.",
  },
  {
    name: 'Emmanuel Macron',
    url: 'https://upload.wikimedia.org/wikipedia/commons/3/32/Emmanuel_Macron_2022.png',
    fact: 'President of France advocating for a strong and united Europe.',
  },
]

export default politicians
