<!-- userOrderPage的子组件：用于用户进行点菜操作以及展示本店铺的菜品 -->

<template>
      <n-card 
      style = "margin-left: auto;
              margin-right: auto;
              width: 95%;">
         <!-- 主体部分，分为首页，商品，评价 -->
        <!-- 商品页 -->
    <el-row class = "foodRowClass">
      <el-col :span="6" v-for="item in info.items">
        <foodCard1 :item="item" :store_id="route.query.store_id"></foodCard1>
      </el-col>
    </el-row>
  </n-card>
</template>

<script setup>
import {reactive, onMounted} from 'vue'
import { NCard } from 'naive-ui'
import {enter_menu} from "@/api/user";
import {useRoute} from "vue-router";
const route = useRoute()

const info = reactive({
  items: []
})

onMounted(() =>{
  enter_menu({
    store_id: route.query.store_id
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