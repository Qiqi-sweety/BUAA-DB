<template>
    <n-card  style="margin-bottom: 50px"  class = "orderSheetCardClass">
        <el-row>
          <el-col :span="14"><h3 class = "orderId">订单号：{{props.order.order_id}}</h3></el-col>
          <el-col :span="10"><p class = "orderTime">日期：{{props.order.time}}</p></el-col>
        </el-row>
        
        <!-- <h3 class = "orderTime">下单时间：2022.10.19</h3> -->
        <el-divider class = "orderDivider"/>

        <n-scrollbar class = "orderScrollbar">
          <div v-for="item in props.order.items">
            <orderSheetFoodCard :item="item.item" :num="item.num"/>
          </div>
        </n-scrollbar>

        <el-row>
            <el-col :span="12"><h3>合计：{{sum}}</h3></el-col>
            <el-col :span="12">
               
            </el-col>
        </el-row>
        
    </n-card>
    
   
</template>



<script setup>
import {NCard, NScrollbar} from 'naive-ui'
import {ref} from "vue";

const showModal = ref(false)
const value = ref(null)
const props = defineProps({
  order: Object
})
const calSum = () => {
  let ans = 0
  props.order.items.forEach(item => {
    ans += item.item.price * item.num
  })
  return ans
}
const sum = ref(calSum())

  </script>

<style>

.orderSheetCardClass {
    width: 320px;
    height: 400px;
    background-color: white;

}

.orderId {
    margin-top: 0;
    margin-bottom: 0;
}

.orderStoreName {
    font-size: 20px;
    margin-top: 0;
    margin-bottom: 0;
}
.orderDivider {
    margin-top: 0;
}
.orderTime {
    margin-top: 2px;
    margin-bottom: 0;
}

.orderScrollbar {
    margin-top: 0;
    height: 230px;
    width: 280px;
    /* border: 2px solid palevioletred; */
}
.orderModelName {
    margin-top: 0;
    font-size: 25px;
}

.orderModelTotal {
    margin-top: 0;
    font-size:20px;
    /* border: 2px solid black;; */
}

.orderModelStar {
    margin-top: 2px;
    height: 50px;
    margin-bottom: 0;
}

.orderModelText {
    margin-top: 0;
    height: 150px;
}


</style>

