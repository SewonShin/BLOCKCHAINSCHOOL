import web3 from './web3';
import CampaignFactory from './build/CampaignFactory.json';

const instance = new web3.eth.Contract(
  JSON.parse(CampaignFactory.interface),
  '0x6ca9E3F44442eD90cFbb3C842DcDE0bBC7955bB0'
);

export default instance;
