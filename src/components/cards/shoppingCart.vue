<template>
    <n-card class = "shoppingCartClass" embedded>
      <el-row>
        <el-col :span="8">
          <img :src="`/api${props.item.image}`" class = "shoppingCartImageClass">
        </el-col>
        <el-col :span="16">
          <h3 class = "shoppingCartName">{{props.item.name}}</h3>
          <el-row>
            <el-col :span="12"><h3 class = "shoppingCartPrice">￥{{price}}</h3></el-col>
            <el-col :span="12">
              <el-input-number v-model="num"
                               :min="0"
                               :max="100"
                               @change="handleChange"
                               class = "numInputClass"/>
            </el-col>
          </el-row>
        </el-col>
      </el-row>
  </n-card>
</template>
  
  <script setup>
  import {NCard} from "naive-ui";
  import {onMounted, ref} from "vue";
  import {add_to_cart, del_from_cart} from "@/api/user";
  import {ElMessage} from "element-plus";

  const props = defineProps({
    item: {},
    store_id: ''
  })
  const num = ref(-1)
  const price = ref(props.item.price * props.item.num)

  const handleChange = (value) => {
    if (props.item.num < value) {
      add_to_cart({
        item_id: props.item.id,
        store_id: props.store_id,
        num: value - props.item.num
      }).then(res => {
        let content = res.data
        console.log(content)
        if (content.code === "200") {
          props.item.num = value
        } else {
          ElMessage({message: content.message, type: "error"})
        }
      })
    } else if (props.item.num > value) {
      del_from_cart({
        item_id: props.item.id,
        store_id: props.store_id,
        num: props.item.num - value
      }).then(res => {
        let content = res.data
        console.log(content)
        if (content.code === "200") {
          props.item.num = value
        } else {
          ElMessage({message: content.message, type: "error"})
        }
      })
    }
  }

  onMounted(() => {
    num.value = props.item.num
  })

  </script>
  
  <style>
  .shoppingCartClass {
    width: 450px;
    height: 150px;
  }

  .shoppingCartImageClass {
    width: 110px;
    height: 110px;
  }

  .shoppingCartName {
    font-size:17px;
  }

  .shoppingCartPrice {
    color: red;
    margin-top: 10px;
  }

  .numInputClass {
    margin-top: 10px;
  }
  
  </style>