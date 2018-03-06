<template>
  <div class="s-head">
    <i class="fa fa-search search-icon"></i>
    <input class="search" id="search" type="text" placeholder="城市名/拼音" v-model="searchValue">
    <span @click="cancel">取消</span>
  </div>
</template>

<script>
  const _ = require('lodash')

  let fakeDic = [
    {value: '张家界', pinyin: 'zhangjiajie'},
    {value: '张家口', pinyin: 'zhangjiakou'},
    {value: '北京', pinyin: 'beijing'},
    {value: '长沙', pinyin: 'changsha'},
    {value: '郑州', pinyin: 'zhengzhou'},
    {value: '北冰洋', pinyin: 'beibingyang'}
  ]

  export default {
    data() {
      return {
        searchValue: '',
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
      getSearchRes: _.debounce(function () {
        let nowValue = this.searchValue;
        let nowReg = new RegExp('^' + nowValue);
        for (let fake of fakeDic) {
          if (nowReg.test(fake.value) || nowReg.test(fake.pinyin)) {

          }
        }
      }, 500)
    }
  }
</script>

<style scoped>
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
</style>
