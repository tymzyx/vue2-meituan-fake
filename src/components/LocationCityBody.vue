<template>
  <div class="body-container">
    <mt-navbar v-model="selected">
      <mt-tab-item id="0">国内</mt-tab-item>
      <mt-tab-item id="1">国际/港澳台</mt-tab-item>
    </mt-navbar>

    <div class="body-wrapper">
      <mt-tab-container v-model="selected">
        <mt-tab-container-item id="0">
          <div class="tab0-head">
            <p>当前: {{selectedCity}}全城</p>
            <p class="change-text" @click="triggerRegion">切换区县</p>
            <i class="fa fa-chevron-down change-text" :class="{'fa-rotate-180': isRegion}" @click="triggerRegion"></i>
          </div>
          <div class="tab0-head-regions" v-show="isRegion">
            <button v-for="i in 6">测试</button>
          </div>
          <div class="tab0-body-detail">
            <p>定位/最近访问</p>
            <button><i class="fa fa-location-arrow"></i>{{locatedCity}}</button>
            <button v-for="c in recentCities">{{c}}</button>
            <p>热门城市</p>
            <button v-for="city in hotCities" @click="selectCity(city.name)">{{city.name}}</button>
          </div>
          <div class="tab0-body-list">
            <index-list v-for="(cityIndex,index) in cityList" :key="index" :index="cityIndex.index" :cities="cityIndex.cities"></index-list>
          </div>
        </mt-tab-container-item>
        <mt-tab-container-item id="1">
          <div class="tab1-wrapper">
            <div class="tab1-left">
              <p v-for="menuInfo,key in internationalMenu" :class="{actived: key == activeKey}"
                 :data-key="key" @click="updateActive">{{menuInfo.name}}</p>
            </div>
            <div class="tab1-right tab1-right-recommend" v-show="isRecommend">
              <div>
                <p>当前定位</p>
                <button><i class="fa fa-location-arrow"></i>北京</button>
              </div>
              <p>最近访问</p>
              <button>上海</button>
              <button>长沙</button>
              <button>张家界</button>
              <p>热门目的地</p>
              <div class="hot-city">香港</div>
              <div class="hot-city">澳门</div>
            </div>
            <div class="tab1-right tab1-right-other" v-show="!isRecommend">
              <div>
                <p>港澳台热门目的地</p>
                <div class="hot-city" v-for="city in internationalHot">{{city.name}}</div>
              </div>
              <div v-for="item in internationalRegions">
                <p>{{item.name}}</p>
                <button v-for="city in item.cities">{{city}}</button>
              </div>
            </div>
          </div>
        </mt-tab-container-item>
      </mt-tab-container>
    </div>
  </div>
</template>

<script>
  // todo 城市搜索国际模块侧边栏高度问题
  import IndexList from './commons/IndexList'

  import {mapState, mapMutations} from 'vuex'

  let fakeInfo = [
    {name: '推荐'},
    {
      name: '港澳台',
      hot: [
        {name: '香港', url: '../assets/hongkong.jpg'},
        {name: '澳门', url: '../assets/hongkong.jpg'},
        {name: '台北', url: '../assets/hongkong.jpg'},
        {name: '高雄', url: '../assets/hongkong.jpg'}
      ],
      regions: [
        {name: '香港', cities: ['香港']},
        {name: '澳门', cities: ['澳门']},
        {name: '台湾', cities: ['台北', '高雄', '台中', '恒春', '新北']}
      ]
    },
    {
      name: '新马泰'
    },
    {
      name: '日韩'
    }
  ];

  export default {
    data() {
      return {
        selected: "0",
        hotCities: [
          {name: '北京'},
          {name: '上海'},
          {name: '石家庄'},
          {name: '深圳'},
          {name: '张家界'},
          {name: '天津'},
          {name: '广州'}
        ],
        cityList: [
          {
            index: 'A',
            cities: [
              {name: '安庆'},
              {name: '安庆'},
              {name: '安庆'},
              {name: '安庆'},
              {name: '安庆'},
              {name: '安庆'},
              {name: '安庆'}
            ]
          },
          {
            index: 'B',
            cities: [
              {name: '北京'},
              {name: '北京'},
              {name: '北京'},
              {name: '北京'},
              {name: '北京'},
              {name: '北京'},
              {name: '北京'}
            ]
          },
          {
            index: 'C',
            cities: [
              {name: '长沙'},
              {name: '长沙'},
              {name: '长沙'},
              {name: '长沙'},
              {name: '长沙'},
              {name: '长沙'},
              {name: '长沙'}
            ]
          }
        ],
        internationalMenu: fakeInfo,
        activeKey: '0',
        isRecommend: true,
        internationalHot: [],
        internationalRegions: [],
        isRegion: false
      }
    },
    computed: {
      ...mapState(['selectedCity', 'locatedCity', 'recentCities'])
    },
    components: {IndexList},
    methods: {
      updateActive(e) {
        let nowKey = e.target.getAttribute('data-key');
        if (nowKey === this.activeKey) {
          return;
        }
        if (nowKey === '0') {
          this.isRecommend = true;
        } else {
          this.isRecommend = false;
          let nowInfo = this.internationalMenu[parseInt(nowKey)];
          this.internationalHot = nowInfo.hot;
          this.internationalRegions = nowInfo.regions;
        }
        this.activeKey = nowKey;
      },
      selectCity(city) {
        this.updateRecentCity();
        this.setCity(city);
        this.$router.push('/');
      },
      triggerRegion() {
        this.isRegion = !this.isRegion;
      },
      ...mapMutations({
        setCity: 'SET_CITY',
        updateRecentCity: 'UPDATE_RECENT_CITY'
      })
    },
    mounted() {
      this.isRegion = false;
    }
  }
</script>

<style>
  .body-container {
    margin-top: 14px;
    border-top: 1px solid #cccccc;
    font-size: 30px;
  }
  .mint-navbar .mint-tab-item {
    padding: 25px 0;
  }
  .mint-tab-item-label {
    font-size: 30px
  }
  .body-wrapper {
    position: relative;
    top: 0;
    bottom: 0;
  }
  .tab0-head {
    width: 100%;
    height: 70px;
    line-height: 70px;
    padding: 10px 30px;
    border-top: 1px solid #cccccc;
  }
  .tab0-head p {
    display: inline;
  }
  .change-text {
    position: relative;
    left: 400px;
    font-size: 26px;
    color: #888888;
  }
  .tab0-body-detail {
    border-top: 1px solid #cccccc;
    border-bottom: 1px solid #cccccc;
    background-color: #eeeeee;
  }
  .tab0-head-regions button, .tab0-body-detail button, .tab1-wrapper button {
    width: 180px;
    height: 80px;
    margin-left: 46px;
    margin-bottom: 20px;
    text-align: center;
    color: #111111;
    cursor: pointer;
    background: white;
    box-sizing: border-box;
    border: 2px solid #dcdfe6;
    border-radius: 4px;
    padding: 6px 13px;
    font-size: 30px;
    outline: none;
  }
  .tab0-body-detail p {
    margin: 20px 30px;
  }
  .tab1-wrapper {
    width: 750px;
    height: 100%;
    overflow: hidden;
    border-top: 1px solid #cccccc;
  }
  .tab1-left {
    width: 20%;
    height: 100%;
    text-align: center;
    float: left;
    background-color: #dddddd;
    clear: both;
  }
  .tab1-left p {
    margin: 0;
    padding: 30px 0;
  }
  .actived {
    background-color: #ffffff;
  }
  .tab1-right {
    width: 80%;
    float: left;
    padding-top: 8px;
  }
  .tab1-right button {
    width: 150px;
    margin-left: 30px;
  }
  .tab1-right p {
    margin: 20px 30px;
    font-size: 28px;
    color: #888;
  }
  .hot-city {
    float: left;
    width: 240px;
    height: 160px;
    border-radius: 16px;
    border: 1px solid #999;
    margin: 10px 10px 30px 30px;
    background: url('../assets/hongkong.jpg');
    background-size: cover;
    text-align: center;
    line-height: 160px;
    color: #fff;
    font-size: 36px;
  }
</style>
