<!-- userOrderPage的子组件：店铺首页的卡片 -->

<!-- 用于展示商家的信息给顾客看 -->
<template>
    <NCard class = "introCardClass">
        <el-row>
            <el-col :span="16">
                <h3 class = "homePageName">{{info.store.name}}</h3>
                <el-row>
                    <el-col :span="12">
                      <el-rate
                          disabled
                          v-model="info.store.star"
                          class = "homePageRateClass"
                          size="large"/>
                    </el-col>
                    <el-col :span="12">
                        <p class = "homePageNumber">销量：{{info.store.sales}}</p>
                    </el-col>
                </el-row>
                <el-divider />
                <p class = "homePageWord">
                    地址：{{info.store.address}}
                </p>
                <p class = "homePageWord">
                介绍：{{info.store.info}}
                </p>


            </el-col>
            <el-col :span="8">
                <img :src="`/api${info.store.logo}`" class = "homePageImageClass">
            </el-col>
        </el-row>
    </NCard>
    <h3 class = "recommendTitle">推荐菜</h3>
    <NCard
    style = " width: 95%;
            margin-top: 20px;
            margin-left: auto;
            margin-right:auto;">
        <el-row class = "recommendCardRow">
            <el-col :span="6" v-for="item in info.hot_items">
              <foodCard2 :food="item" :store_id="route.query.store_id"></foodCard2>
            </el-col>
        </el-row>
    </NCard>

</template>

<script setup>
  import {reactive, onMounted} from 'vue'
  import {NCard} from 'naive-ui'
  import {enter_store} from "@/api/userMain";
  import {useRoute} from "vue-router";

  const info = reactive({
    store: {},
    hot_items: [],
  })
  const route = useRoute()

  onMounted(() => {
    enter_store({
      store_id: route.query.store_id
    }).then(res => {
      let content = res.data
      console.log(content)
      if (content.code === "200") {
        info.store = content.info
        content.items.forEach(item => {
          info.hot_items.push(item)
        })
      }
    })
  })

</script>

<style>
.introCardClass {
 width: 95%;
 /* height: 100px; */
 margin-left: auto;
 margin-right: auto;
}


.homePageImageClass {
    margin-top: 50px;
    width: 450px;
    height: 450px;
}

.homePageName {
    margin-left: 100px;
    margin-bottom: 0;
    font-size: 40px;
}

.homePageRateClass {
    margin-left: 100px;
    margin-top: 20px;
}

.homePageWord {
    font-size: 20px;
    color: gray;
    margin-left: 100px;
    margin-right: 20px;
}

.homePageNumber {
    font-size: 20px;
    color: gray;
}

.recommendTitle {
    margin-left: 50px;
    font-size: 25px;
    margin-top:20px;
    margin-bottom: 0px;
}

.recommendCardRow {
    margin-left:60px;
}


</style>