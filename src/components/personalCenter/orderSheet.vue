<!-- personalCenter的子组件：用于展示用户的订单 -->

<!-- TODO：根据该用户的订单信息list，实例化orderSheetCard1的list，并展示 -->

<template>
    <el-row class = "orderSheetRowClass">
      <el-col :span="6" v-for="order in info.orders">
        <orderSheetCard1 :order="order"/>
      </el-col>
    </el-row>
</template>

<script setup>
import {onMounted, reactive} from 'vue'
import {show_orders} from "@/api/user";
import {ElMessage} from "element-plus";

const info = reactive({
  orders: []
})

onMounted(() => {
  show_orders().then(res => {
    let content = res.data
    console.log(content)
    if (content.code === "200") {
      content.list.forEach(item => {
        info.orders.push(item)
      })
    } else {
      ElMessage({message: content.message, type: "error"})
    }
  })
})

</script>


