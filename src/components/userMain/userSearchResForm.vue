<!-- userMainPage的子组件：搜索结果组件 -->

<!-- TODO:根据搜索返回的list，构建展示卡，将结果进行展示
如果是按照店铺搜索，则建立storeCard1；
如果是按照商品搜索，则建立storeCard2； -->

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
              <div v-for="(item, index) in stores" :key="index">
                <el-col style = "padding-right: 0;" :span="12">
                  <store-card1
                      :storeLogoUrl="item.logo"
                      :storeName="item.name"
                      :time="'?'"
                      :star="item.star"
                      :number="item.sales"
                  ></store-card1>
                </el-col>
              </div>
              <div v-for="(item, index) in this.food" :key="index">
                <el-col style = "padding-right: 0;" :span="12">
                  <store-card2
                      :storeLogoUrl="item.logo"
                      :storeName="item.name"
                      :time="'?'"
                      :star="item.star"
                      :number="item.sales"
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
  import {user_search} from "@/api/userMain";


  
  export default {
    name: 'userSearchResForm',
    props: {
      key: {type: String, required: true},
      label: {type: String, default: "商品"}
    },
    components: {
      storeCard2,
      storeCard1,
    },
    methods: {
    },
    setup(props) {
      const stores = [
        {'id': 789012, 'name': "这是店名2", 'address': "这是地址2",
          'logo': "/media/144d6d9c-9157-4010-bd23-594ef753f0ca.jpg", 'info': "这是信息2", 'star': 4, 'sales': 888},
      ];
      const food = [];
      user_search({type: props.label, msg: props.key})
          .then(res => {
            let content = res.data
            console.log(content)
            if (content.code === "200") {
              if (content.label === "店铺") {
                // stores = content.list
              } else {
                // food = content.list
              }
            }
          })
      return {
        stores, food
      }
    }
  }
</script>
