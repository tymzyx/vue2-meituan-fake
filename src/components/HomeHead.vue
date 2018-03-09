<template>
  <div class="homeHead">
    <div class="homeContainer">
      <div class="weather-wrapper">
        <i :class="weatherIcon"></i>
        <span>{{weatherTmp}}</span>
      </div>
      <div class="city-wrapper">
        <span class="city" @click="selectCity">{{selectedCity}}</span>
        <i class="fa fa-chevron-down" @click="selectCity"></i>
      </div>
      <div class="search-wrapper">
        <i class="iconfont icon-search search-icon" @click="toSearch"></i>
        <input class="search" type="text" placeholder="搜索" @click="toSearch">
      </div>
      <div class="plus-wrapper">
        <i class="iconfont icon-pluslarge" @click="triggerPlus"></i>
      </div>
    </div>
    <div class="plus-detail-wrapper" v-show="isPlus">
      <div class="plus-detail-item" v-for="item,index in plusInfo" :class="{divided: index!=3}">
        <i :class="item.icon"></i>
        <span>{{item.text}}</span>
      </div>
    </div>
  </div>
</template>

<script>
  import {mapState, mapMutations} from 'vuex'

  const $ =require('jquery');

  const weatherIcons = {
    '晴': 'iconfont icon-qing',
    '阴': 'iconfont icon-yin',
    '雪': 'iconfont icon-xue',
    '云': 'iconfont icon-duoyun'
  };

  let plusInfo = [
    {text: '扫一扫', icon: 'iconfont icon-saoyisao'},
    {text: '付款码', icon: 'iconfont icon-erweima1'},
    {text: '开发票', icon: 'iconfont icon-fapiaoguanli1'},
    {text: '骑单车', icon: 'iconfont icon-bicycle1'}
  ]

  export default {
    data() {
      return {
        weatherIcon: '',
        weatherTmp: '',
        plusInfo: plusInfo,
        isPlus: false, // plus框是否显现
      }
    },
    methods: {
      selectCity() {
        this.$router.push('/locationCities');
      },
      toSearch() {
        this.$router.push('/searchMain')
      },
      triggerPlus() {
        this.isPlus = !this.isPlus;
      },
      getWeather() {
        let _this = this;
        let weatherUrl = "https://free-api.heweather.com/s6/weather/now?parameters";
        $.ajax({
          url: weatherUrl,
          dataType: "json",
          type: "post",
          data: {
            location: this.selectedCity,
            key: '6e2712c19f8d437bb4bd52548d0ffae3'
          },
          success: function(res) {
            let weatherState = res['HeWeather6'][0]['now']['cond_txt'];
            for (let state in weatherIcons) {
              let reg = new RegExp(state);
              if (reg.test(weatherState)) {
                _this.weatherIcon = weatherIcons[state];
                break;
              }
            }
            _this.weatherTmp = res['HeWeather6'][0]['now']['tmp'] + '°';
          }
        });
      },
      ...mapMutations({
        setCity: 'SET_CITY',
        locatingCity: 'LOCATING_CITY'
      })
    },
    computed: {
      ...mapState(['selectedCity'])
    },
    mounted() {
      this.isPlus = false;
      if (this.selectedCity !== '') {
        this.getWeather();
        return;
      }
      let _this = this;
      $.getScript('http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=js',
        function() {
          if (remote_ip_info.ret === 1) {
            let cityName = remote_ip_info.province;
            _this.setCity(cityName);
            _this.locatingCity(cityName);
            _this.getWeather();
          }
        }
      );
    }
  }
</script>

<style scoped>
  .homeHead {
    width: 750px;
    height: 80px;
    padding-top: 10px;
    background-color: white;
    position: absolute;
    top: 0;
    border-bottom: 1px solid #ccc;
    z-index: 1;
  }
  .homeContainer {
    width: 100%;
    height: 100%;
    display: flex;
  }
  .weather-wrapper {
    width: 80px;
    text-align: center;
  }
  .weather-wrapper i {
    font-size: 44px;
    display: block;
  }
  .weather-wrapper span {
    font-size: 20px;
    position: relative;
    bottom: 10px;
  }
  .city-wrapper {
    line-height: 80px;
    width: 140px;
    text-align: center;
  }
  .search-wrapper {
    line-height: 80px;
    text-align: center;
    position: relative;
  }
  .search-icon {
    position: absolute;
    left: 14px;
  }
  .search {
    background-color: #eeeeee;
    border: none;
    border-radius: 27px;
    height: 54px;
    padding-left: 54px;
    width: 380px;
    outline: none;
    -webkit-tap-highlight-color: rgba(0,0,0,0);
  }
  .plus-wrapper {
    line-height: 80px;
    text-align: center;
    width: 80px;
  }
  .plus-wrapper i {
    font-size: 44px;
  }
  .plus-detail-wrapper {
    position: absolute;
    width: 220px;
    height: 360px;
    background: rgba(128, 128, 128, 0.95);
    right: 24px;
    top: 112px;
    border-radius: 20px;
    border: 1px solid rgba(128, 128, 128, 0.95);
    display: flex;
    flex-direction: column;
    padding: 0 30px;
    box-sizing: border-box;
  }
  .plus-detail-wrapper:before {
    content: "";
    position: absolute;
    right: 20px;
    top: -26px;
    width: 0;
    height: 0;
    border-top: 13px solid transparent;
    border-right: 13px solid transparent;
    border-left: 13px solid transparent;
    border-bottom: 13px solid rgba(128, 128, 128, 0.95);
  }
  .plus-detail-item {
    height: 90px;
    text-align: center;
    line-height: 90px;
    color: #fff;
  }
  .plus-detail-item span {
    font-size: 28px;
  }
  .plus-detail-item i {
    font-size: 36px;
  }
  .divided {
    border-bottom: 0.01em solid #aaa
  }
</style>
