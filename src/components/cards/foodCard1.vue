<!-- 可以加入购物车的商品展示卡 -->

<!-- 位于userOrderPage -->

<!-- 需要动态初始化的值:
  1.商品图片
  2.商品名称
  3.销量
  4.价格 -->


<template>
    <n-card class = "foodCardClass1" embedded>
      <template #cover>
        <img :src= "`/api${props.item.image}`" class = "foodCardImageClass1">
      </template>
      <h3 class = "foodCardName">{{props.item.name}}</h3>
      <p class = "foodCardNumber">销量：{{props.item.sales}}</p>
      <el-row class = "foodCardRow">
        <el-col :span="12"><h3 class = "foodCardPrice">￥{{props.item.price}}</h3></el-col>
        <el-col :span="12">
          <n-button class = "joinButtonClass" type="warning" size = "medium" @click="addToCart">
            加入购物车
          </n-button>
        </el-col>
      </el-row>
      

    </n-card>
  </template>

<script setup>
import {NCard, NButton} from 'naive-ui'
import {add_to_cart} from "@/api/user";
import {ElMessage} from "element-plus";

const props = defineProps({
  item: Object,
  store_id: String,
})
const addToCart = () => {
  add_to_cart({
    store_id: props.store_id,
    item_id: props.item.id
  }).then(res => {
    let content = res.data
    console.log(content)
    if (content.code === "200") {
      ElMessage({
        message: "已将 ["+props.item.name+"] 加入购物车",
        type: "success"
      })
    } else {
      ElMessage({
        message: content.message,
        type: "error"
      })
    }
  })
}
</script>

<style>

.foodCardName {
  margin-top: 0;
  font-size: 20px;
  margin-bottom: 0;
}

.foodCardNumber {
  margin-top: 0;
  margin-bottom: 0;
}

.joinButtonClass {
  margin-top: 5px;
  margin-left: 20px;
}

.foodCardPrice {
  color: red;
  margin-top: 5px;
  margin-bottom: 0;
}

.foodCardRow {
  margin-top: 0;
  margin-bottom: 0;
}
.foodCardClass1 {
    width: 300px;
    height: 430px;
    padding-bottom: 0;
}

.foodCardImageClass1 {
    width: 300px;
    height: 300px;
}

</style>