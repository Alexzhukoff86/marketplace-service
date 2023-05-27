import grpc

from books_shared.utils import logger
from books_shared.utils.config import Config
from books_shared.protopy.account_pb2 import GetAccountRequest, GetAccountResponse, google_dot_protobuf_dot_empty__pb2
from books_shared.protopy.account_pb2_grpc import AccountServiceStub

class Client:
    def __init__(self):
        account_server_channel = grpc.insecure_channel(f"{Config.account_server}:{Config.account_server_port}")
        self.account_client = AccountServiceStub(account_server_channel)

    def get_account(self, id):
        get_account_request = GetAccountRequest(id=id)
        get_account_response = self.account_client.GetAccount(get_account_request)
        return get_account_response.account

    def get_accounts(self):
        empty = google_dot_protobuf_dot_empty__pb2.Empty()
        accounts = self.account_client.GetAccountList(empty)
        return accounts.accounts
