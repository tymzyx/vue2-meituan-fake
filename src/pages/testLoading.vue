<template>
  <div class="testIndex">
    <my-scroll :page="page" :on-refresh="onRefresh" :on-pull="onPull">
      <div slot="scrollList">
        <ul>
          <li v-for="(x,index) in list" :key="index">列表</li>
        </ul>
      </div>
    </my-scroll>
  </div>
</template>
<script type="text/javascript">
  import myScroll from '../components/ScrollLoading'

  export default {
    data() {
      return {
        list: [],
        page: {
          counter: 1,
          pageStart: 1,
          pageEnd: 1,
          total: 10
        },
      }
    },
    methods: {
      onRefresh(mun) { //刷新回调
        setTimeout(() => {
          this.$root.$emit('setState', 3)
        }, 500)
      },
      onPull(mun) { //加载回调
        if (this.page.counter <= this.page.total) {
          setTimeout(() => {
            this.page.counter++
            this.$root.$emit('setState', 5)
            for (let i = 0; i < 10; i++) {
              this.listdata.push({})
            }
          }, 500)
        } else {
          this.$root.$emit('setState', 7)
        }
      },

    },
    components: {
      myScroll
    },
    created() {

    },
    mounted() {
      for (let i = 0; i < 1 * 50; i++) {
        this.list.push({})
      }

    },

  }
</script>
<style lang="less" scoped>
  .testIndex {
    color: #000;
  }
</style>
