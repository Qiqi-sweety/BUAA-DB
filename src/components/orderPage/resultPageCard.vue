<!-- userOrderPage的子组件：搜索框搜索店内商品的商品结果展示界面 -->

<template>
    <h3
    style = "margin-left: 50px;
    font-size: 25px;
    margin-top:20px;
    margin-bottom: 0;">
        
        搜索结果</h3>
    <n-card 
      style = "margin-left: auto;
              margin-right: auto;
              width: 95%;">

      <el-row class = "foodRowClass">
        <el-col :span="6" v-for="item in info.items">
          <foodCard1 :item="item" :store_id="route.query.store_id"></foodCard1>
        </el-col>
      </el-row>
    </n-card>
</template>

<script setup>
import {reactive, onMounted} from 'vue'
import { NCard} from 'naive-ui'
import {enter_search} from "@/api/user";
import {useRoute} from "vue-router";
const route = useRoute()

const info = reactive({
  items: []
})

onMounted(() => {
  enter_search({
    store_id: route.query.store_id,
    msg: route.query.msg,
  }).then(res => {
    let content = res.data
    console.log(content)
    if (content.code === "200") {
      content.items.forEach(item => {
        info.items.push(item)
      })
    }
  })
})


</script>
<style>

.foodRowClass {
  margin-left : 50px;
}

</style>