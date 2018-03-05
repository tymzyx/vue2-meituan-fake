<template>
  <div class="body-container">
    <mt-navbar v-model="selected" class="updateFont">
      <mt-tab-item id="0">国内</mt-tab-item>
      <mt-tab-item id="1">国际/港澳台</mt-tab-item>
    </mt-navbar>

    <mt-tab-container v-model="selected">
      <mt-tab-container-item id="0">
        <div class="tab0-head">
          <p>当前: 北京全城</p>
          <p class="change-text">切换区县</p> <i class="fa fa-chevron-down change-text"></i>
        </div>
        <div class="tab0-body-detail">
          <p>定位/最近访问</p>
          <button><i class="fa fa-location-arrow"></i>北京</button>
          <button>上海</button>
          <button>长沙</button>
          <button>张家界</button>
          <p>热门城市</p>
          <button v-for="city in hotCities">{{city.name}}</button>
        </div>
        <div class="tab0-body-list">
          <index-list v-for="cityIndex in cityList" :index="cityIndex.index" :cities="cityIndex.cities"></index-list>
        </div>
      </mt-tab-container-item>
      <mt-tab-container-item id="1">
        <mt-cell v-for="n in 5" title="tab-container 2"></mt-cell>
      </mt-tab-container-item>
    </mt-tab-container>
  </div>
</template>

<script>
  import IndexList from './commons/IndexList'

  export default {
    data() {
      return {
        selected: "0",
        hotCities: [
          {name: '北京'},
          {name: '北京'},
          {name: '北京'},
          {name: '北京'},
          {name: '北京'},
          {name: '北京'},
          {name: '北京'}
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
          }
        ]
      }
    },
    components: {IndexList}
  }
</script>

<style>
  .body-container {
    margin-top: 14px;
    border-top: 1px solid #cccccc;
    font-size: 30px;
  }
  .tab0-body-detail button {
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
  .mint-navbar .mint-tab-item {
    padding: 25px 0;
  }
  .mint-tab-item-label {
    font-size: 30px
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
    left: 320px;
    font-size: 26px;
    color: #888888;
  }
  .tab0-body-detail {
    border-top: 1px solid #cccccc;
    border-bottom: 1px solid #cccccc;
    background-color: #eeeeee;
  }
  .tab0-body-detail p {
    margin: 20px 30px;
  }
</style>
