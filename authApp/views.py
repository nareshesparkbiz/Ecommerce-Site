from django.shortcuts import render
from .serializers import UserRegisterSerializer, UserProfileSerializer, UserLoginSerializer, UserChangePasswordSerializer, UserAddressSerializer, UserPaymentSerializer
from .models import UserAddress, UserPayment, MyUser
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from .renderer import UserRenderer
from rest_framework.generics import UpdateAPIView


# Create your views here.


def get_tokens_for_user(user):
    try:

        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
    except Exception as e:
        print(e)


def get_or_none(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None





class RegisterView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        try:

            serializer = UserRegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        'message': 'Register Successfully',
                        'status': status.HTTP_201_CREATED
                    }
                )
            return Response({
                'message': serializer.errors,
                'status': status.HTTP_400_BAD_REQUEST
            })

        except Exception as e:
            return Response({
                'message': 'Backened API Error',
                'error': str(e),
                'status': status.HTTP_404_NOT_FOUND
            })


class LoginView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        try:

            serializer = UserLoginSerializer(data=request.data)

            if serializer.is_valid():
                email = serializer.data.get('email')
                password = serializer.data.get('password')
                check_user = authenticate(email=email, password=password)

                if check_user is not None:
                    token = get_tokens_for_user(check_user)
                    
                    return Response(
                        {
                            'token': token,
                            'message': "Login Successfully",
                            'status': status.HTTP_200_OK
                        }
                    )
                return Response({
                    'message': 'Invalid Email or Password',
                    'status': status.HTTP_400_BAD_REQUEST
                })

            return Response(
                {
                    'message': serializer.errors,
                    'status': status.HTTP_400_BAD_REQUEST
                }
            )
        except Exception as e:
            return Response({
                'message': 'Backened API Error',
                'error': str(e),
                'status': status.HTTP_404_NOT_FOUND
            })


class ForgotPasswordView(APIView):
    renderer_classes = [UserRenderer]

    def put(self, request, format=None):
        try:

            result = request.data
            print(result)
            user = get_or_none(MyUser, email=result['email'])

            if user is not None:

                serializer = UserChangePasswordSerializer(
                    user, data=result, partial=True)

                if serializer.is_valid():
                    serializer.save()
                    return Response(
                        {
                            'message': 'Password Changed Successfully',
                            'status': status.HTTP_200_OK
                        }
                    )
                return Response({
                    'message': serializer.errors,
                    'status': status.HTTP_400_BAD_REQUEST
                }
                )

            return Response({
                'message': 'Invalid Email Address',
                'status': status.HTTP_400_BAD_REQUEST
            })
        except Exception as e:
            return Response({
                'message': 'Backened API Error',
                'error': str(e),
                'status': status.HTTP_404_NOT_FOUND
            })


class ProfileView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request, *args, **kwargs):
        try:
            print(request.user.id)
            serializer = UserProfileSerializer(request.user)
            userAdd = UserAddress.objects.filter(user_id=request.user.id)
            userPay = UserPayment.objects.filter(user_id=request.user.id)
            # userPay=get_or_none(UserPayment,user_id=serializer.data.id)

            addSerializer = UserAddressSerializer(userAdd, many=True)
            paySerializer = UserPaymentSerializer(userPay, many=True)
            # print(addSerializer)

            return Response({
                'message': 'Profile Data',
                'data': {'user': serializer.data,
                         'add': addSerializer.data,
                         'pay': paySerializer.data
                         },
                'status': status.HTTP_200_OK
            })

        except Exception as e:
            return Response({
                'message': 'Backened API Error',
                'error': str(e),
                'status': status.HTTP_404_NOT_FOUND
            })

    def put(self, request, pk=None):
        try:

            result = request.data
            userProf = get_or_none(MyUser, id=pk)
            if userProf is not None:
                serializer = UserProfileSerializer(
                    userProf, data=request.data, partial=True)
                # print(serializer,"data")

                if serializer.is_valid():
                    id1 = serializer.save()
                    print(id1, "id1")
                    # UpdateAddress()

                    return Response(
                        {
                            'message': 'Profile saved successfully',
                            'status': status.HTTP_200_OK
                        }
                    )
                return Response(
                    {
                        'message': serializer.errors,
                        'status': status.HTTP_400_BAD_REQUEST
                    }
                )
            return Response(
                {
                    'message': f'Id {pk} doesnot exist',
                    'status': status.HTTP_404_NOT_FOUND
                }
            )
        except Exception as e:

            return Response({
                'message': 'Backened API Error',
                'error': str(e),
                'status': status.HTTP_404_NOT_FOUND
            })


class UpdateAddress(APIView):
    #  authentication_classes=[JWTAuthentication]

    def put(self, request, pk=None):
        try:

            addData = UserAddress.objects.filter(id=pk).first()
            print(addData, "adddata")
            serializer = UserAddressSerializer(
                addData, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        'msg': 'Address Update SuccessFully',
                        'status': status.HTTP_200_OK
                    }
                )
            return Response({
                'message': serializer.errors,
                'status': status.HTTP_400_BAD_REQUEST
            })
        except Exception as e:

            return Response({
                'message': 'Backened API Error',
                'error': str(e),
                'status': status.HTTP_404_NOT_FOUND
            })

    def post(self, request, format=None):
        try:
            print(request.user.id, "user")
            formData = request.data
            formData['user_id'] = request.user.id

            serilaizer = UserAddressSerializer(data=formData)

            if serilaizer.is_valid():
                serilaizer.save()
                return Response(
                    {
                        'message': "Address saved successfully",
                        "status": status.HTTP_201_CREATED
                    }
                )
            return Response({
                "message": UserAddressSerializer.errors,
                "status": status.HTTP_400_BAD_REQUEST
            })

        except Exception as e:

            return Response({
                'message': 'Backened API Error',
                'error': str(e),
                'status': status.HTTP_404_NOT_FOUND
            })

    def delete(self, request, pk=None):
        try:

            userAdd = get_or_none(UserAddress, id=pk)
            if userAdd is not None:

                userAdd.delete()
                return Response({
                    'message': "User Address deleted successfully",
                    "status": status.HTTP_200_OK
                })

            return Response({
                'message': f"Given Id {pk} is Invalid ",
                "status": status.HTTP_400_BAD_REQUEST
            })
        except Exception as e:

            return Response({
                'message': 'Backened API Error',
                'error': str(e),
                'status': status.HTTP_404_NOT_FOUND
            })


class UserpaymentView(APIView):
    authentication_classes=[JWTAuthentication]
    def post(self, request, *args, **kwargs):
        try:

            formData = request.data
            formData['user_id'] = request.user.id

            serializer = UserPaymentSerializer(data=formData)

            if serializer.is_valid():
                serializer.save()

                return Response(
                    {
                        'message': "User Payment Details saved successfully",
                        "status": status.HTTP_201_CREATED
                    }
                )

            return Response(
                {
                    'message': serializer.errors,
                    "status": status.HTTP_400_BAD_REQUEST
                }
            )

        except Exception as e:
            return Response({
                'message': 'Backened API Error',
                'error': str(e),
                'status': status.HTTP_404_NOT_FOUND
            })

    def put(self, request, pk=None):
        try:
            paymentdata = get_or_none(UserPayment, id=pk)

            if paymentdata is not None:
                serializer = UserPaymentSerializer(
                    paymentdata, data=request.data, partial=True)

                if serializer.is_valid():
                    serializer.save()
                    return Response(
                        {
                            'msg': 'Payment Details  Update SuccessFully',
                            'status': status.HTTP_200_OK
                        }

                    )

                return Response(
                    {
                        'msg': serializer.errors,
                        'status': status.HTTP_400_BAD_REQUEST
                    }
                )
            return Response(
                {
                    'msg': f'Given Id  {pk} is invalid',
                    'status': status.HTTP_404_NOT_FOUND
                }
            )

        except Exception as e:

            return Response({
                'message': 'Backened API Error',
                'error': str(e),
                'status': status.HTTP_404_NOT_FOUND
            })

    def delete(self, request, pk=None):
        try:
            data = get_or_none(UserPayment, id=pk)

            if data is not None:
                data.delete()
                return Response({
                    'message': 'Payment Details deleted successfully',

                    'status': status.HTTP_200_OK

                })
            return Response({
                'message': f'Id {pk} is Invalid',
                
                'status': status.HTTP_404_NOT_FOUND
            })

        except Exception as e:
            return Response({
                'message': 'Backened API Error',
                'error': str(e),
                'status': status.HTTP_404_NOT_FOUND
            })
