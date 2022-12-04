<template>
    <el-row class = "orderSheetFoodCardRow">
        <el-col :span="7">
            <img :src="`/api${props.item.image}`" class = "orderSheetfoodCardImage">
        </el-col>
        <el-col :span="11">
            <h3 class = "orderSheetFoodName">{{props.item.name}}</h3>
            <p class = "orderSheetFoodNumber">×{{props.num}}</p>
        </el-col>
        <el-col :span="6">
            <h3 class = "orderSheetFoodPrice">￥{{props.num * props.item.price}}</h3>
        </el-col>
    </el-row>
</template>



<script setup>

const props = defineProps({
  item: Object,
  num: Number
})


</script>

<style>

.orderSheetFoodCardRow {
    height: 80px;
    margin-top: 0;
    /* border: 2px solid black; */
}

.orderSheetfoodCardImage {
    width: 70px;
    height: 70px;
    margin-left: 0%;
    margin-top: 0%;
    padding-left: 0%;
    /* border: 2px solid black; */
}

.orderSheetFoodName {
    margin-top: 0%;
    font-size: 15px;
    /* margin-bottom: 5px; */
}

.orderSheetFoodNumber {
    margin-top: 0%;
    color: grey;
}

.orderSheetFoodPrice {
    margin-top: 0%;
}


</style>