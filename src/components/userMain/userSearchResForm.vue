<!-- userMainPage的子组件：搜索结果组件 -->

<template>
    <el-form>
      <el-form-item
      style = "width: 1200px;
              background-color: white;
              border-radius: 10px;
              margin: auto;">

<el-form style = "width: 100%;">
      <el-form-item style = "height: 60px;
        width: 100%;">
            <h3 
            style = "font-size: 30px;
                    margin-top : 10px;
                    margin-left : 3%;">
              搜索结果
            </h3>

            
          </el-form-item>
          <el-form-item style = "padding: 3% 2.5% 3% 3%;">
            <el-row style = "width: 100%;">
              <div v-for="(item, index) in info.stores" :key="index">
                <el-col style = "padding-right: 0;" :span="12">
                  <store-card1 :store="item"></store-card1>
                </el-col>
              </div>
              <div v-for="(item, index) in info.food" :key="index">
                <el-col style = "padding-right: 0;" :span="12">
                  <store-card2
                      :store="item.store"
                      :items="item.items"
                  ></store-card2>
                </el-col>
              </div>
<!--              <el-col style = "padding-right: 0%;" :span="12"><store-card2/></el-col>-->
<!--              <el-col style = "padding-right: 0%;" :span="12"><store-card2/></el-col>-->
            </el-row>
            

          </el-form-item>
        </el-form>

      </el-form-item>
    </el-form>
</template>

<script>
  import storeCard2 from "../cards/storeCard2.vue"
  import storeCard1 from "../cards/storeCard1.vue"
  import {user_search} from "@/api/user";
  import {reactive} from "vue";
  import {useRoute} from "vue-router"
  import {ElMessage} from "element-plus";
  
  export default {
    name: 'userSearchResForm',
    components: {
      storeCard2,
      storeCard1,
    },
    methods: {
    },
    setup() {
      const info = reactive({
        stores: [
          // {'id': 123456, 'name': "这是店名1", 'address': "这是地址1",
          //   'logo': "/media/2eecdd44-55ae-42d0-9764-f82b979d59a4.jpg", 'info': "这是信息1", 'star': 5, 'sales': 321},
          // {'id': 789012, 'name': "这是店名2", 'address': "这是地址2",
          //   'logo': "/media/144d6d9c-9157-4010-bd23-594ef753f0ca.jpg", 'info': "这是信息2", 'star': 4, 'sales': 888},
        ],
        food: [
          {
            store: {},
            items: [
              // {'id': 111, 'name': "这是商品1", 'price': 11, 'image': "/media/2eecdd44-55ae-42d0-9764-f82b979d59a4.jpg",
              //   'info': "这是店铺介绍", 'sales': 123},
              // {'id': 222, 'name': "这是商品2", 'price': 22, 'image': "/media/2eecdd44-55ae-42d0-9764-f82b979d59a4.jpg",
              //   'info': "这是店铺介绍", 'sales': 123},
              // {'id': 333, 'name': "这是商品3", 'price': 33, 'image': "/media/2eecdd44-55ae-42d0-9764-f82b979d59a4.jpg",
              //   'info': "这是店铺介绍", 'sales': 123}
            ]
          }
        ]
      })
      const route = useRoute()

      user_search({
        msg: route.query.key,
        type: route.query.label,
      }).then(res => {
        let content = res.data
        console.log(content)
        info.stores = []
        info.food = []
        if (content.code === "200") {
          if (route.query.label === "店铺") {
            content.list.forEach(item => {
              info.stores.push(item)
            })
            console.log("店铺:")
            console.log(info.stores)
          } else {
            content.list.forEach(item => {
              info.food.push(item)
            })
            console.log("商品:")
            console.log(info.food)
          }
        } else if (content.code === "404") {
          content.list.forEach(item => {
            info.stores.push(item)
          })
          ElMessage(content.message)
        }
      })
      return {
        info
      }
    }
  }
</script>
