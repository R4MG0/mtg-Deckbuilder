export interface CommanderCard {
  uuid: string;
  name: string;
  cmc: number;
  colors: string[];
  colorIdentity: string[];
  image_uris: {
    art_crop: string;
    border_crop: string;
    large: string;
    normal: string;
    png: string;
    small: string;
  }
  keywords: string[];
  mana_cost: string;
  power: number;
  toughness: number;
}
