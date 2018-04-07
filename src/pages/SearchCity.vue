<template>
  <div class="sc-container">
    <div class="s-head">
      <i class="fa fa-search search-icon"></i>
      <input class="search" id="search" type="text" placeholder="城市名/拼音" v-model="searchValue">
      <span @click="cancel">取消</span>
    </div>
    <div class="body-wrapper">
      <div v-for="i in searchList" class="item" @click="selectCity(i)"><span>{{i}}</span></div>
    </div>
  </div>
</template>

<script>
  import {mapMutations} from 'vuex'

  const _ = require('lodash');

  let fakeDic = [
    {value: '张家界', pinyin: 'zhangjiajie'},
    {value: '张家口', pinyin: 'zhangjiakou'},
    {value: '北京', pinyin: 'beijing'},
    {value: '长沙', pinyin: 'changsha'},
    {value: '郑州', pinyin: 'zhengzhou'},
    {value: '北冰洋', pinyin: 'beibingyang'}
  ];

  export default {
    data() {
      return {
        searchValue: '',
        searchList: new Array(15)
      }
    },
    mounted() {
      this.searchInput = document.getElementById("search");
      this.searchInput.focus();
    },
    watch:{
      searchValue() {
        this.getSearchRes();
      }
    },
    methods: {
      cancel() {
        this.$router.push('/locationCities')
      },
      getSearchRes: _.debounce(function () {  // 根据输入框内容匹配结果，_.debounce控制判断频率
        let nowValue = this.searchValue;
        for (let i = 0; i < 15; i++) {
          this.$set(this.searchList, i, '');
        }
        if (nowValue === '') {
          return;
        }
        let nowReg = new RegExp('^' + nowValue);
        let matchCount = 0;
        for (let fake of fakeDic) {
          if (nowReg.test(fake.value) || nowReg.test(fake.pinyin)) {
            matchCount += 1;
            if (matchCount > 15) {
              break;
            }
            this.$set(this.searchList, matchCount-1, fake.value);
          }
        }
        if (matchCount === 0) {
          for (let i = 0; i < 15; i++) {
            this.$set(this.searchList, i, '');
          }
        }
      }, 500),
      selectCity(city) {
        this.updateRecentCity();
        this.setCity(city);
        this.$router.push('/');
      },
      ...mapMutations({
        setCity: 'SET_CITY',
        updateRecentCity: 'UPDATE_RECENT_CITY'
      })
    }
  }
</script>

<style scoped>
  .sc-container {
    height: 100%;
    position: relative;
  }
  .s-head {
    width: 750px;
    height: 80px;
    padding-top: 10px;
    line-height: 80px;
  }
  .s-head span {
    font-size: 30px;
    color: dodgerblue;
  }
  .search-icon {
    position: relative;
    left: 66px;
    z-index: 1;
  }
  .search {
    position: relative;
    left: 10px;
    background-color: #eeeeee;
    border: none;
    border-radius: 27px;
    height: 64px;
    padding-left: 54px;
    width: 530px;
    outline: none;
    -webkit-tap-highlight-color: rgba(0,0,0,0);
    margin-right: 30px;
  }
  .body-wrapper {
    width: 100%;
    position: absolute;
    top: 80px;
    bottom: 0;
    border-top: 1px solid #bbb;
    margin-top: 20px;
    text-align: center;
  }
  .item {
    height: 6%;
    width: 90%;
    text-align: left;
    font-size: 30px;
    margin: auto;
    border-bottom: 1px solid #ddd;
    position: relative;
  }
  .item span {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    -webkit-transform: translateY(-50%);
    -o-transform: translateY(-50%);
    -moz-transform: translateY(-50%);
    -ms-transform: translateY(-50%);
  }
</style>
