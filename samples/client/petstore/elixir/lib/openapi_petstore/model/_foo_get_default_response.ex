# NOTE: This file is auto generated by OpenAPI Generator 6.1.1-SNAPSHOT (https://openapi-generator.tech).
# Do not edit this file manually.

defmodule OpenapiPetstore.Model.FooGetDefaultResponse do
  @moduledoc """
  
  """

  @derive [Poison.Encoder]
  defstruct [
    :string
  ]

  @type t :: %__MODULE__{
    :string => OpenapiPetstore.Model.Foo.t | nil
  }
end

defimpl Poison.Decoder, for: OpenapiPetstore.Model.FooGetDefaultResponse do
  import OpenapiPetstore.Deserializer
  def decode(value, options) do
    value
    |> deserialize(:string, :struct, OpenapiPetstore.Model.Foo, options)
  end
end

