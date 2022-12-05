<template>
    <n-card style = "width: 700px;height: 400px;">
        <el-row>
            <el-col :span="16">
                <el-row style = "margin-bottom: 0%;">
                    <el-col :span="6">
                        <h3 style = "font-size: 20px;">店铺头像：</h3>
                    </el-col>
                    <el-col :span="18">
                        <img :src="`/api${props.store.logo}`" style = "width: 80px;height: 80px;">
                    </el-col>
                    
                </el-row>
                <el-row style = "margin-top: 0%;margin-bottom: 0%;">
                    <el-col :span="6"><h3 style = "font-size: 20px;">店铺名：</h3></el-col>
                    <el-col :span="18"><p style = "font-size: 20px;">{{props.store.name}}</p></el-col>
                </el-row>
                <el-row style = "margin-top: 0%;margin-bottom: 0%;">
                    <el-col :span="6"><h3 style = "font-size: 20px;">店铺地址：</h3></el-col>
                    <el-col :span="18"><p style = "font-size: 20px;">{{props.store.address}}</p></el-col>
                </el-row>
                <el-row style = "margin-top: 0%;margin-bottom: 0%;">
                    <el-col :span="6"><h3 style = "font-size: 20px;">店铺介绍：</h3></el-col>
                    <el-col :span="18"><p style = "font-size: 20px;">{{props.store.info}}</p></el-col>
                </el-row>
            
            </el-col>
            <el-col :span="8">
                <img :src="`/api${props.store.license}`" style = "width: 220px;height: 150px;">
                <n-button size = "large" round type="warning" style = "margin-top: 100px;margin-left: 80px;" @click="validate">
                审核通过
                </n-button>
            </el-col>
        </el-row>

    </n-card>
</template>

<script setup>
import {show_orders} from "@/api/user";
import {ElMessage} from "element-plus";

const props = defineProps({
  store: {}
})
const validate = () => {
  show_orders({
    store_id: props.store.id
  }).then(res => {
    let content = res.data
    console.log(content)
    info.orders = []
    if (content.code === "200") {
      ElMessage({message: "处理成功", type: "success"})
    } else {
      ElMessage({message: content.message, type: "error"})
    }
  })
}
</script>