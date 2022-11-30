from src.modules.create_order.create_order_usecase import CreateOrderUsecase

class CreateOrderController:
    def __init__(self, usecase: CreateOrderUsecase):
        self.createOrderUsecase = usecase