import React, {Component} from 'react';
import {
View,
Text,
Image,
TouchableOpacity,
SafeAreaView,
ScrollView,
} from 'react-native';
import colors from '../../config/color';
import {connect} from 'react-redux';
import {REC_LOADING} from '../actions/recommendactions';
import AsyncStorage from '@react-native-community/async-storage';
import Recommendations from './Recommendations';
import AwsRecommendations from './AwsRecommendations';
import ProgressIndicator from '../../components/ProgressIndicator';

class CloudRecommendations extends Component {
static navigationOptions = ({navigation}) => {
return {
title: navigation.getParam('Title', 'Recommendations'),
headerStyle: {
backgroundColor: navigation.getParam('BackgroundColor', '#fcfdfc'),
},
headerTintColor: navigation.getParam('HeaderTintColor', '#000000'),
headerTitleStyle: {
fontWeight: navigation.getParam('fontWeight', 'bold'),
},
};
};
state = {
CloudSelect: 1,
loading: false,
};

AzureRecommend = ({onPress, CloudSelect}) => (
<TouchableOpacity onPress={() => onPress()}>
<View
style={{
          width: 162,
          height: 55,
          backgroundColor: CloudSelect ? '#ffffff' : '#efefef',
          borderRadius: 8,
          elevation: CloudSelect ? 4 : null,
          justifyContent: 'center',
          alignItems: 'center',
        }}>
{CloudSelect ? (
<Image
source={require('../../image/azure.png')}
style={{
              tintColor: CloudSelect ? null : null,
              height: 25,
              width: 25,
            }}
/>
) : (
<Image
source={require('../../image/AZURE_BW.png')}
style={{height: 25, width: 30}}
/>
)}
</View>
</TouchableOpacity>
);

AwsRecommend = ({onPress, CloudSelect}) => (
<TouchableOpacity onPress={() => onPress()}>
<View
style={{
          width: 162,
          height: 50,
          backgroundColor: CloudSelect ? '#ffffff' : '#efefef',
          borderRadius: 8,
          elevation: CloudSelect ? 4 : null,
          justifyContent: 'center',
          alignItems: 'center',
        }}>
{CloudSelect ? (
<Image
source={require('../../image/AWS.png')}
style={{
              tintColor: CloudSelect ? null : null,
              height: 25,
              width: 35,
            }}
/>
) : (
<Image
source={require('../../image/AWS_BW.png')}
style={{height: 27, width: 32}}
/>
)}
</View>
</TouchableOpacity>
);

componentDidMount = async () => {
await this.recommendApiData();
// this.goToAzureRec();
};

recommendApiData = async () => {
//console.log('coming to the recommen API Data Cloud page');
this.setState({
loading: true,
});
try {
const tenant = await this.gettingTenantID();

      if (tenant !== null) {
        console.log('tenant mil gya');
        const datarec = {
          tenantID: tenant,
          customerID: this.props.users.customerID,
        };
        this.props.d({
          type: REC_LOADING,
          payload: datarec,
        });
        this.goToAzureRec();
        this.setState({
          loading: false,
        });
      } else {
        this.props.navigation.navigate('AddAzure');
        this.setState({
          loading: false,
        });
        Toast.show("You don't have any tenant add account");
      }
    } catch (error) {}

};

gettingTenantID = async () => {
return new Promise(resolve =>
setTimeout(() => {
const tenantCode = AsyncStorage.getItem('tenantID');
resolve(tenantCode);
}),
);
};

goToAzureRec = () => {
return <Recommendations navigation={this.props.navigation} />;
};

goToAwsRec = () => {
return <AwsRecommendations navigation={this.props.navigation} />;
};

render() {
return (
<SafeAreaView style={{flex: 1}}>
<View
style={{
            backgroundColor: colors.white,
            borderRadius: 8,
            marginTop: 8,
            width: '100%',
            height: 63,
            marginHorizontal: 10,
          }}>
<View style={{flexDirection: 'column'}}>
<View
style={{
                flexDirection: 'row',
                justifyContent: 'space-around',
                alignItems: 'center',
                marginTop: 4,
                marginBottom: 4,
              }}>
<this.AzureRecommend
CloudSelect={this.state.CloudSelect == 1}
onPress={() => this.setState({CloudSelect: 1})}
/>

              <this.AwsRecommend
                CloudSelect={this.state.CloudSelect == 2}
                onPress={() => this.setState({CloudSelect: 2})}
              />
            </View>
          </View>
        </View>

        <ScrollView style={{marginTop: 5}}>
          {this.state.CloudSelect == 1 && this.goToAzureRec()}
          {this.state.CloudSelect == 2 && this.goToAwsRec()}
        </ScrollView>
        {this.state.loading && <ProgressIndicator />}
      </SafeAreaView>
    );

}
}

export default connect(
state => {
return {
users: state.userReducer.users,
recData: state.recommendReducer.recData,
loading: state.recommendReducer.loading,
error: state.recommendReducer.error,
};
},

d => {
return {
d: d,
};
},
)(CloudRecommendations);
